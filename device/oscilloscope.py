import pyvisa
import numpy as np


class Oscilloscope:
    rm_ = pyvisa.ResourceManager()

    def __init__(self, interface):  # 接続先を指定
        self._scope = self.rm_.open_resource(interface)

    def fetch(self, channel):  # 波形を取得するチャンネル名指定，例fetch(1)

        self._scope.write(f'DATA:SOU CH{channel}')
        self._scope.write('DATA:WIDTH 2')
        self._scope.write('DATA:ENC SRIBINARY')

        self._scope.write('DATa:STARt 1')
        # 取得するデータ箇所指定(十分すぎるくらいとっている)
        self._scope.write('DATa:STOP 10000000000')

        ymult = float(self._scope.query('WFMOUTPRE:YMULT?'))  # y-axis least
        # y-axis zero error
        yzero = float(self._scope.query('WFMOUTPRE:YZERO?'))
        yoff = float(self._scope.query('WFMOUTPRE:YOFF?'))   # y-axis offset
        xincr = float(self._scope.query('WFMP:XINCR?'))  # x-axis least count
        xoff = int(self._scope.query('WFMP:PT_OFF?'))    # x-axis offset

        ADC_wave = self._scope.query_binary_values(
            'CURVe?', datatype='h', is_big_endian=False, container=np.array)
        Volts = (ADC_wave - yoff) * ymult + yzero
        time = np.linspace(-1*xincr*xoff, -1*xincr*xoff +
                           len(Volts)*xincr, len(Volts), endpoint=False)

        return time, Volts

    def average(self, count):  # averaging数指定
        return self._scope.write(f':ACQ:MOD AVE;:ACQ:NUMAV {count};')

    def get_max(self, channel):
        [times, volts] = self._scope.fetch(channel)
        return max(volts)

    def get_pk2pk(self, channel):
        [times, volts] = self._scope.fetch(channel)
        return max(volts)-min(volts)

    def sample(self):
        return self._scope.write('ACQ:MOD SAM')
