'''
#test rock paper scissors assignment, run this file to check your solution
# (right click, run 'check_rock_paper_scissors')

note that if you get a error trace that ends like this: ( note the <<<< notes)

 File "/Users/username/PycharmProjects/cs22/RockPaperScissorsProject/test_post.py", line 113, in t_run
    exec(open(path).read(), globals())        <<<<
  File "<string>", line 21, in <module>       <<<<  line number will be in your file
ValueError: substring not found               <<<<  this is the error message about that line in your program


Then you will need to run yor rock_paper_scissors.py program independent from the check_ program
To locate the problem. The once it seems to run, go back and run the check_ program

-----

if you get a EOF error like this:
  File "/Users/gjenkins/Dropbox/PycharmProjects/cs22_asssignments/RockPaperScissorsProject/test_post.py", line 25, in input
    raise EOFError("You program is trying to input user input, but there is no more userinput in the test")
EOFError: You program is trying to input user input, but there is no more userinput in the test

you are probably not stopping your program when the user types Q or q as required

'''

from test_post import *

_DEBUG = False

cases = "rpsRPS"*5 + "Q"
in_str = ''.join( [ x+'\n' for x in cases] )
def report_error(out,index,error):
    print("Your OUPUT up to error detected:\n" + "-"*40)
    print(out[0:index+1])
    print("-"*40)
    print(error,"\n")
    print("Your OUPUT after error was detected:\n" + "-"*40)
    print(out[index:])
    print("-"*40)


def test(out):
    index = 0
    errors = 0
    prompt = re.compile( r'quit\s*(|\?|:)\s*$', re.MULTILINE | re.IGNORECASE )
    found_quit = False

    for i,u in enumerate(cases):
        m = prompt.search(out,index)
        if  m: # found new prompt
            if found_quit: # user has input Q
                report_error(out, index, "*** your program did quit after user type q or Q")
                errors += 1
                break
        else: # no prompt, but did not process Q
            if found_quit:
                break
            else: # no prompt and have not processed quit
                report_error(out, index, "*** could not find a user prompt with word 'quit'")
                errors += 1
                break
        # found prompt
        if _DEBUG: print("DDD",out[index:m.end()], "<<< found prompt")
        # look for user input
        index = m.end()
        m = re.compile(u).search(out,index)
        if m is None:
            report_error(out,index,'*** user input {} not located\n  do you have a input statement?'.format(u))
            errors += 1
            break
        if u.lower() == 'q':
            found_quit = True
            continue

        if _DEBUG: print("DDD", out[index:m.end()], "<<< found promt")

        # find line with computer choose  rock paper or scissors
        index = m.end()
        r = re.compile(r"^\s*computer .*(rock|paper|scissors)\s*$", re.MULTILINE | re.IGNORECASE)
        m = r.search(out,index)
        if m is None:
            # print("out at {} index is:\n".format(index))
            # print(out[index:index+100],"...\n")
            report_error(out,index,"*** can't find  Computer picked rock paper or scissor line")
            errors += 1
            break
        if _DEBUG: print('DDD Computer picked {}'.format(m.groups()[0]), "user picked",u)
        computer = m.groups()[0][0].lower()
        letters = 'rps'
        c =letters.index(computer)
        # print ("***", computer)
        u = letters.index(u.lower())
         #print ("***", u)
        w = (c + 1) % 3 == u
        l = (u + 1) % 3 == c
        o = 'tie'
        if w: o = 'win'
        if l: o = 'lose'
        if _DEBUG: print("DDD should be you",o)
        index = m.end()
        r = re.compile(r"^\s*you\s+(lose|win|tie).*computer,*$", re.MULTILINE | re.IGNORECASE)
        m = r.search(out, index)
        if m is None:
            # print("out at {} index is:\n".format(index))
            # print(out[index:index + 100], "...\n")
            report_error(out,index,"*** can't find  'you {} against the computer' line")
            errors +=1
            break
        # print('***you {}'.format(m.groups()[0]))
        if o != m.groups()[0].lower():
            report_error(out,index,"*** Your program should have said you {}".format(o))
            errors += 1
            break;


    return errors


def main():
    errors = 0
    # time in seconds to time out
    print("\nyour program output will only be shown if you have errors\n")
    run('rock_paper_scissors.py', test=test, stdin=in_str, time=5, output=False)


if __name__ == '__main__':
    main()

