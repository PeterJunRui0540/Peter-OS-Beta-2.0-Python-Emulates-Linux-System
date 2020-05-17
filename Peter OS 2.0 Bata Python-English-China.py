import turtle



print('Weicome To Use Peter OS 1.0 Bata Python System')
Boot = float(input('Whether or not to use Peter OS 1.0 Bata Python System，Please Press The Boot 1 ，Shut Down Please Press Any Key（1 except）。Please Write：'))
if (Boot == 1):
    print('The Computer Has Been Booted,Please Select The Software To Use。', '1.Phone', '2.E-mall', '3.Transfer', '4.Update', '5.Draw', '6.Coming Soon')
    Software = int(input('Please Enter：'))
    if (Software == 1):
        print('The Phone Is Open,Please Enter The Number You Want To Dial')
        Boot = str(input('Please Enter：'))
        print('Is Dialing', input())
        Hung = int(input('To Hang Up,Press 1.Please Enter：'))
        if (Hung == 1):
            print('Has Been Hung Up')
    if (Software == 2):
        print('The E-mall Has Been Opened.Please Enter The Receiver:')
        Emall = str(input('Please Enter：'))
        Send = str(input('Please Enter What You Want To Send：'))
        print('Has Been Sent To The', Emall, Send)
    if (Software == 3):
        print('The Transfer Has Been Opened.Please Enter The Beneflciary Account：')
        Beneflciary = str(input('Please Enter The Beneflciary Account：'))
        Amount = str(input('Please Enter The Amount：'))
        print('Transferred', Beneflciary, Amount)
    if (Software == 4):
        print('Checking For Updates')
        print('An Important Update Was Found 。Is It An Update ？')
        Update = int(input('Press 1 For Conflrmation Or 1 For Cancellation。Please Press ：'))
        if (Update == 1):
            print('Updating')
            print('Download Completed')
            print('Run Peter OS Update.deb File')
            print('The Update Was Successful And Restarting ，Please Start Running。')
else:
    print('Computer Was Shut Down')
