import cv2 as cv2
from datetime import datetime
from spot_diff import spot_diff
import time
import numpy as np

def record1(count):
    print('#')
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'stolen/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc, 20.0, (640, 480))

    while True:
        count = count + 1
        _, frame = cap.read()

        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    0.6, (255, 255, 255), 2)

        out.write(frame)
        if count == 250:
            return




        # if cv2.waitKey(1) == 27:
        #     cap.release()
        #     cv2.destroyAllWindows()
        #     break


def find_motion():
    motion_detected = False
    is_start_done = False

    cap = cv2.VideoCapture(0)

    check = []

    print("waiting for 2 seconds")
    time.sleep(0.1)
    frame1 = cap.read()

    _, frm1 = cap.read()


    frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY )

    while True:
        _, frm2 = cap.read()
        if frm2 is None:
            break
        frm2 = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY )


        diff = cv2.absdiff(frm1, frm2)

        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY )

        contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        # look at it
        contors = [c for c in contors if cv2.contourArea(c) > 25]

        print(contors)

        if len(contors) > 5:
            # cv2.putText(thresh, "motion detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

            record1(0)
            continue


            motion_detected = True
            is_start_done = False

        elif motion_detected and len(contors) < 3:
            # record1(0)
            # continue

            if (is_start_done) == False:
                start = time.time()
                is_start_done = True
                end = time.time()

            end = time.time()

            print(end - start)
            if (end - start) > 4:
                frame2 = cap.read()
                cap.release()
                cv2.destroyAllWindows()
                x = spot_diff(frame1, frame2)
                if x == 0:
                    print("running again")
                    return

                else:

                    print("found motion")
                    return

        else:
            cv2.putText(thresh, "no motion detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)



        # cv2.imshow("winname", thresh)

        _, frm1 = cap.read()
        if frm1 is None:
            break

        frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY )

        if cv2.waitKey(1) == 27:
            break
    find_motion()
    return