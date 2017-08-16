#!/bin/bash
sleep 15
rostopic pub -1 /fr_order face_recognition/FRClientGoal -- 1 "none"
echo "RECONOCEDOR INICIADO"
