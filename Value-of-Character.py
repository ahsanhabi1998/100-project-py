# Python এর ord() ফাংশন হলো একটি বিল্ট-ইন ফাংশন যা ক্যারেক্টারগুলির জন্য ইউনিকোড মান পেতে ব্যবহার করা হয়। যখন একটি ক্যারেক্টার ord() ফাংশনে পাঠানো হয়, এটি একটি ইন্টিজার মান ফেরত দেয়  এই ফাংশনটি একটি স্ট্রিং গ্রহণ করে  উদাহরণস্বরূপ, ord('a') ইন্টিজার 97 ফেরত দেয়, ord('€') (ইউরো চিহ্ন) 8364 ফেরত দেয়2। এটি chr() এর উল্টো ফাংশন যা 8-বিট স্ট্রিং এবং ইউনিকোড অবজেক্টগুলির জন্য ইউনিকোড পয়েন্ট প্রতিস্থাপন করে3।


a = ""
print ("the ascii value of",a ,ord(a))