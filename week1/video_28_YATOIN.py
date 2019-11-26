while True:
    try:
        number = int(input("Enter your favorite number boss\n"))
        print(18/number)
        break
    except ValueError:
        print('MAke sure you enter the correct number')
    except ZeroDivisionError:
        print("Don't pick 0")
    except:
        break
    finally:
        print("loop complete")