# Date: 02/23/2019
# Original passgen author: Mohamed
# Some changed by: UnderMind0x41
# Description: A social engineering password generator
# This script required python version >= 3.0
import argparse
import sys

max_count_default = 1000000
max_count_main_default = 1000

class PassGen:

    def __init__(self, max_count=max_count_default, max_count_main=max_count_main_default, silent=False):
        self.pet = None
        self.child = None
        self.spouse = None
        self.target = None
        self.passwords = []
        self.silent = silent
        self.max_count = max_count
        self.max_count_main = max_count_main
    
    def prompt(self, txt):
        return str(input(txt))

    def question(self, target):
        answers = {}

        answers['firstname'] = self.prompt('Enter {}\'s first name: '.format(target))
        answers['lastname'] = self.prompt('Enter {}\'s last name: '.format(target))
        answers['nickname'] = self.prompt('Enter {}\'s nick name: '.format(target))

        while True:
            bday = self.prompt('Enter {}\'s birthday (dd.mm.yyyy): '.format(target))

            if not len(bday.strip()):
                break

            if len(bday.split('.')) != 3:
                print('Invalid birthday format\n')
                continue
            
            for _ in bday.split('.'):
                if not _.isdigit():
                    print('Birthday only requires numbers\n')
                    continue
            
            dd, mm, yyyy = bday.split('.')
            
            if int(mm) > 12 or int(mm) < 1 \
            or int(dd) > 31 or int(dd) < 1 \
            or len(yyyy) != 4:
                print('Invalid birthday\n')
                continue
            
            bday = { 'day': dd, 'month': mm, 'year': int(yyyy) }
            break 
            
        answers['birthday'] = bday
        return answers   

    def cases(self, word):
        return [word.lower(), word.title()]    
    
    def fullname(self, fname, lname):
        return ['{}{}'.format(a, b) for a in self.cases(fname) for b in self.cases(lname)]

    def format_names(self):
        for _ in range(self.max_count_main):
            if not self.silent:
                print(f'Generated: {len(self.passwords)}')

            iters = 0
            for data in [self.target, self.spouse, self.child, self.pet]:

                for n in ['firstname', 'lastname', 'nickname']:

                    fullname_list = []
                    name = data[n].strip()

                    if not len(name):
                        continue
                    
                    if not iters:
                        fullname_list = self.fullname(data['firstname'], data['lastname'])
                        iters += 1
                    
                    for word in self.cases(name) + fullname_list:

                        a, b, c = ('{}{}'.format(word, _), 
                                  '{}{}'.format(_, word), 
                                  '{0}{1}{0}'.format(_, word)
                                  )

                        if not word in self.passwords:
                            self.passwords.append(word)

                        if not a in self.passwords:
                            self.passwords.append(a)
                        
                        if not b in self.passwords:
                            self.passwords.append(b)

                        if not c in self.passwords:
                            self.passwords.append(c)

                        bday = data['birthday']

                        if bday:
                            d, e, f, g, h, i, j, k, l, m, n, o, p, q = (
                                '{}{}'.format(word, bday['year']),
                                '{}{}'.format(bday['year'], word),
                                '{}{}{}{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}.{}.{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}{}{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}.{}.{}{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}_{}{}{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}_{}.{}.{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}{}_{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}.{}.{}_{}'.format(bday['day'], bday['month'], bday['year'], word),                                
                                '{}-{}{}{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}-{}.{}.{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}{}-{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}.{}.{}-{}'.format(bday['day'], bday['month'], bday['year'], word),

                            )

                            if not d in self.passwords:
                                self.passwords.append(d)
                            
                            if not e in self.passwords:
                                self.passwords.append(e)
                            
                            if not f in self.passwords:
                                self.passwords.append(f)

                            if not g in self.passwords:
                                self.passwords.append(g)   
   
                            if not h in self.passwords:
                                self.passwords.append(h)
      
                            if not i in self.passwords:
                                self.passwords.append(i)
                            
                            if not j in self.passwords:
                                self.passwords.append(j)
                            
                            if not k in self.passwords:
                                self.passwords.append(k)

                            if not l in self.passwords:
                                self.passwords.append(l)   
   
                            if not m in self.passwords:
                                self.passwords.append(m)

                            if not n in self.passwords:
                                self.passwords.append(n)
                            
                            if not o in self.passwords:
                                self.passwords.append(o)
                            
                            if not p in self.passwords:
                                self.passwords.append(p)

                            if not q in self.passwords:
                                self.passwords.append(q)     
        
    def generator(self, ignore_additional = True):
        self.target = self.question('target')  
        print('\n')

        self.spouse = self.question('spouse')
        print('\n')

        self.child = self.question('child')
        print('\n')

        self.pet = self.question('pet')
        print('\n')

        print('Generating main passwords... \nIt\'s may take a while.')
        self.format_names()
        if self.silent:
            print("...generated {} main passwords".format(len(self.passwords)))

        output_file = '{}.txt'.format(self.target['firstname'].lower()
                             if self.target['firstname'] else 'pass.txt')

        with open(output_file, 'wt') as f:
            for pwd in self.passwords:
                if not self.silent:
                    print('Writing ...')
                f.write('{}\n'.format(pwd))

        if not ignore_additional:
            print("Generating additionals combinations...")
            with open(output_file, 'at') as f:
                i = 0
                while(i < self.max_count):
                    if not self.silent:
                        print('Writing additional combinations ... {}/{}'.format(i*3, self.max_count*3))
                    f.write('{}{}\n'.format(self.target['firstname'], i))
                    f.write('{}{}\n'.format(self.target['lastname'], i))
                    f.write('{}{}\n'.format(self.target['nickname'], i))
                    i += 1
            if self.silent:
                print("...generated {} additional combinations".format(self.max_count*3))

        print('Passwords Generated in file: {}'.format(output_file))
        quit()


def parseCmdArgs(argv):
    parser = argparse.ArgumentParser(description='Run password generator')
    parser.add_argument('--ignore-additional', dest='ignore_additional', action='store_true',
                        help='ignore additions combinations')
    parser.add_argument('--max-count', dest='max_count', default=max_count_default,
                        help='maximum count for additional combinations')
    parser.add_argument('--max-count-main', dest='max_count_main', default=max_count_main_default,
                        help='maximum count for main combinations')
    parser.add_argument('--silent', dest='silent', action='store_true',
                        help='no print process (faster)')
    parser.set_defaults(ignore_additional=False)
    parser.set_defaults(silent=False)
    args = parser.parse_args(argv[1:])
    return args

if __name__ == '__main__':
    args = parseCmdArgs(sys.argv)
    PassGen(max_count=int(args.max_count),
            max_count_main=int(args.max_count_main),
            silent=args.silent
            ).generator(ignore_additional=args.ignore_additional)
