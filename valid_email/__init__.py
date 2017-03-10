import valid_email as valid

def run():
    email = valid.check()

    ID = raw_input()

    print email.run_check(ID)
    run()


if __name__ == '__main__':

    run()
    
