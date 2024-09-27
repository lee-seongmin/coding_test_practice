from MovingControl import *
import time
import RPi.GPIO as GPIO
import ultraSonic as us

TRIG_PIN = 23 # BCM 
ECHO_PIN = 24 # BCM
MOTOR_ADDR = 0x16
I2C_BUS = 1


def main():
    #(1) 핀 명명법 설정
    GPIO.setmode(GPIO.BCM)

    #(2) 센서 연결 핀 동작모드 설정 및 초기값
    us.initUltra(TRIG_PIN, ECHO_PIN)
    myCar = MovingCar(MOTOR_ADDR, I2C_BUS)
    myCar.Car_Stop()
    print('MyCar init OK.')
    time.sleep(1)

    try:
        while True:
            dis = us.getDistance(TRIG_PIN, ECHO_PIN)
            print(dis)

            if dis >= 50:
                print("Run")
                myCar.Car_Run(50, 50)
                time.sleep(1)
            else:
                print("right")
                myCar.Car_Right(0, 50)
                time.sleep(1)

        
        
    except KeyboardInterrupt:

        print("Stop")
        myCar.Car_Stop() 
        time.sleep(1)    

        print('강제종료')


print("Play Moving")
main()
print('End')