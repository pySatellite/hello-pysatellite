# hello-pysatellite
- The Python program I'm distributing for the first time

![image](https://github.com/pySatellite/hello-pysatellite/assets/87309910/deac5b33-3d3d-45e3-8e50-47f1a881955b)

View at:
- https://pypi.org/project/hello-pysatellite

### INSTALL
```bash
$ pip install hello-pysatellite
```

### USE
```bash
$ hello-pysatellite-pic


                                                  .:^:.
                                                ^!~~~~!!
                                               ~!^^^^~!7
                                               7!!!7!?J~^^^:.
                                             .^7!~~~~~^~~~~~~~~^.
                                            :!~~~7???!~~~~~~~~~~!~:
                                           ^7~~~~~~^^~~~~~~~~~~~~~!!~^~~~~^:
                                        .:^!~~~~^^^~~~~~~~~~~~~~~^^~?7~~~~~!^
                                     .^~~~~^~~~~!Y!^^^^~~~~~~~~~~??^~J!~~~~!~
                                    :!~~~~~~~~~~?Y!~!!~~^~~~~~~~~~5!^7!!!!~^
                                    7~~~~~~~~~~~^^^JGGPY?~~~^^~~~^!!!!
                                   .?^~~~~~!J7~~~~^5&&&&P7~^?J^~~~^!7
                                 .^!5~~~~~~^J~~~~~~~7J?7!~~~YJ~~~~^7:
                                ~J5YP!^~~~~^??^~~~~~^^^^^~^~^^~~~~~~^
                                J5Y5P5~^^~~~~J?~^^^^^~^^~!?~~~~~~~~~!.
                                :JP555Y?!~^~~^7??7!!!!!!77!~~~~~~~^~!
                              ^?YYY5555Y5Y?~^~^~~!!!!!!~~^^~~~~^^^!!.
                            .?5Y5PYYYYYYYY5Y7^~~~^^^^^^^^^^^^^~!?Y~
                          .~J5YYP5YYYYYYYYYY5J^^~^^^~~~!!!!7?Y555?.
                         !Y5YY55YYYYYYYYYYYYY5J~~!7JJYYYYY55555557.
                         ?P5Y55YYYYYYYYYYYYYYY5YY5YYYY55PPGGP555YYY:
                        :7?5P5YYYYYYYYYYYYYY5555YYY555PP55YYYY5PYYYY.
                        !~^!P555555YYYYYYYYYYYY55555YYYYYYYYYYY55YYYY^
                       .7^~~JP?~!7?Y555YYYYYYYYYYYYYYYYYYYYYYYY5GYY55!.
                       .J~~~~J~~^^^^~7JY555YYYYYYYYYYYYYYYYY55Y??5Y7~~!.
                        ~?~^!7^~~~~~^^^~!7JYY5555555555555YJ?!~^^77^~~~~
                         :7!?!^~~~~~~~~~^^^^~~!77?????77!~~^^^~~~^?!^~~!
                           :7!^~~~~~~~~~~~~~~~^^^^^^^^^^^~~~~~~~~~~?~~7:
                            :7^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^7?!.
                             7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^!^
                             :!^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^!.
                              ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
```

### DEV
```bash
$ git clone ...
$ cd hello-pysatellite
$ pdm venv create
$ source .venv/bin/activate
(hello-pysatellite-3.8) $ pdm install
```

### TEST
```bash
$ pdm add -dG test pytest pytest-cov
$ pytest
$ pytest -s
$ pytest --cov

```

### DEPLOY 
```bash
$ pdm publish
```

### Contributing
```bash
$ git branch 0.2.0/very-small-function

$ git checkout 0.2.0/very-small-function
Switched to branch '0.2.0/very-small-function'

$ vi pyproject.toml

$ git status
On branch 0.2.0/very-small-function
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   pyproject.toml

no changes added to commit (use "git add" and/or "git commit -a")

$ git add .
$ git status
On branch 0.2.0/very-small-function
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   pyproject.toml

$ git commit -m "start dev 0.2.0"
[0.2.0/very-small-function 4ed0751] start dev 0.2.0
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
fatal: The current branch 0.2.0/very-small-function has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin 0.2.0/very-small-function

$ git push --set-upstream origin 0.2.0/very-small-function
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 287 bytes | 287.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for '0.2.0/very-small-function' on GitHub by visiting:
remote:      https://github.com/pySatellite/hello-pysatellite/pull/new/0.2.0/very-small-function
remote:
To github.com:pySatellite/hello-pysatellite.git
 * [new branch]      0.2.0/very-small-function -> 0.2.0/very-small-function
Branch '0.2.0/very-small-function' set up to track remote branch '0.2.0/very-small-function' from 'origin'.
```

### REF
- image to text : https://www.text-image.com/convert/ascii.html
