import pygame

import controller

import ctypes as C

dll = C.cdll.LoadLibrary('DLLTEST.dll')

dll.controller_init();




k=0.3;#x y比例系数
kt=0.2#torque 比例系数

while(1):
    control_data=controller.rocket.get_val()
    forceX=control_data[0]
    forceY=-control_data[1]
    torque=-control_data[2]
    thrust=-control_data[3]

    ch1=0.6666*forceX*k+torque*kt;
    ch2=(-0.3333*forceX-forceY/1.7321)*k+torque*kt;
    ch3=(-0.3333*forceX+forceY/1.7321)*k+torque*kt;
    ch4=0.6666*thrust+0.3333;

    print(ch1,ch2,ch3,ch4)

    #dll.trans(int(ch1),int(ch2),int(ch3),int(ch4));
    controller.clock.tick(20)


    







