import sys
bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
...................................................................."""



print("Enter message you want to print with BitMap")
message = input("-->")


if message == '':
    sys.exit()


for line in bitmap.splitlines():
    for i , bit in enumerate(line):
        if bit == ' ':
            print(' ',end='')
        else:
            print(message[i % len(message)] , end='')
    print()