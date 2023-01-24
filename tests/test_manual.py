from codeinsights.dump import make_output

whitelist = [r'C:\Users\User\Desktop\pythonstuff\traceback\tests\data\foo.txt', r'C:\Users\User\Desktop\pythonstuff\traceback\tests\data\bar.txt']

make_output(whitelist, r'C:\Users\User\Desktop\pythonstuff\traceback\tests\data', r'C:\Users\User\Desktop\pythonstuff\traceback\tests\tmp\output')