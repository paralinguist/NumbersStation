# NumbersStation
A simple numbers station using faux OTP

Disclaimer:
Most of the codec code is written by students (this was their project for an expo). Treat it gently - it is the code of learners, not grizzled professionals.
Most of the io code is written by me. Treat it gently - it is the code of someone who hasn't been a grizzled professional for a while now.

Yes, the initial version of this station broadcast using the FM transmitter bug that was built into the first RPi.
Yes, that was naughty, and when we found out, we switched to an actual FM transmitter (with diminished range, but legal).

Where are the number wavs? Welp, they're recordings of a student's voice, and I'm not comfortable uploading them.
You could use wav recordings of a text-to-speech bot or yourself. If you'd like to submit your own records for public use, I'd love that. I'll get around to doing it myself one day.

How do you get the OTP key?
You can generate one by rolling dice, using random.org or using my OTP generator: https://otp.atar.tools/
Please please please - don't trust some random guy's key generator on the Internet for anything real. 

This is designed to be a demonstration, not for real world use.

On that note, real one-time pads do not get used multiple times (hence, "one-time"), it would be a simple matter to provide the tool with either a much longer OTP to delete as it uses it, or simply broadcast a pre-encrypted set of numbers (safer). This is, again, for demonstration - it is DESIGNED to be decrypted and used easily, not fit for actual secret transmissions.

Re: music
Obviously any music will do. For the curious, we used "Butterflying" by Elena Kats-Chernin, "Hector Steps Out" by Peter McConnel and part of the London Philharmonic Orchestra's rendition of Korobeiniki (the Tetris theme).
