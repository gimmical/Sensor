import Adafruit_GPIO.SPI as SPI
import Adafruit_GPIO.MCP3008 as MCP

# MCP3008のSPIポートとチャンネルを指定してMCP3008オブジェクトを作成
SPI_PORT = 0
SPI_DEVICE = 0
mcp = MCP.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# FSR connected to adc #0
FSR_CHANNEL = 0

# 測定時間とサンプリング周期の設定
T = 15   # 測定時間（秒）
Ts = 0.5 # サンプリング周期（秒）

# 測定と出力
for _ in range(int(T / Ts)):
    # アナログデータの読み取り
    measured_value = mcp.read_adc(FSR_CHANNEL)
    # 出力
    voltage = measured_value * 5.0 / 1023
    print(f"Voltage = {voltage:.4f}")
    time.sleep(Ts)