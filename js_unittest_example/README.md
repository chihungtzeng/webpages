Example of running unittest for javascripts.

Prerequisite
--

```
cd $HOME
emerge nodejs  # My OS is Gentoo. For other systems, use apt or rpm etc.
npm karma
npm karma-firefox-launcher
npm jasmine
```

After executing the commands, we can run ~/node_modules/karma/bin/karma
to invoke the testing procedures.

Setup karma
--
```
cd /path/to/your_js_directory
~/node_modules/karma/bin/karma init  # Interactive way to generate karma.conf.js
```
We can edit karma.conf.js whenever needed later on.

Run tests
--

The repo has two toy javascripts, sum.js and test/test_sum.js. The former
contains the program logic while the latter, writen in jasmine syntax, tests
the logic.

To run the tests, simply

```
cd /path/to/your_js_directory
CHROME_BIN=/usr/bin/chromium ~/node_modules/karma/bin/karma start karma.conf.js
```

My system installs open source version of chrome (i.e., chromium), so I have to setup CHROME_BIN=/usr/bin/chromium. Other people might not bother to do this.

Once invoking the above command, the following message would show up:
```
11 12 2017 10:38:12.189:INFO [karma]: Karma v1.7.1 server started at http://0.0.0.0:9876/
11 12 2017 10:38:12.191:INFO [launcher]: Launching browsers Chrome, Firefox with unlimited concurrency
11 12 2017 10:38:12.200:INFO [launcher]: Starting browser Chrome
11 12 2017 10:38:12.206:INFO [launcher]: Starting browser Firefox
11 12 2017 10:38:12.671:INFO [Chrome 62.0.3202 (Linux 0.0.0)]: Connected on socket BBtxOPMCewHfMtBLAAAA with id 39387210
Chrome 62.0.3202 (Linux 0.0.0): Executed 1 of 1 SUCCESS (0.01 secs / 0.004 secs)
11 12 2017 10:38:13.837:INFO [Firefox 52.0.0 (Linux 0.0.0)]: Connected on socketChrome 62.0.3202 (Linux 0.0.0): Executed 1 of 1 SUCCESS (0.01 secs / 0.004 secs)
Firefox 52.0.0 (Linux 0.0.0): Executed 1 of 1 SUCCESS (0.001 secs / 0.003 secs)
TOTAL: 2 SUCCESS
```

That's it. Happy testing! :smile:

[Site index](../)
