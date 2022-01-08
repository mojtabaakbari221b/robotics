### در اینجا توضیحاتی از طریقه ارتباط با رابط های نوشته شده قرار میگیرد

##### ارتباط با مدل گروه (مانند رباتها،‌ ماشین ابزار کنترل عددی و ...)

* لیستی از همه گروه ها
```
/group/
```

* گرفتن یک گروه با آیدی خاص
```
/group/<num:id>/
/group/?id=<num>/
```

* گرفتن یک گروه دارای عنوان خاص
```
/group/?title__exact=<str>/
/group/?title__icontains=<str>
/group/?title__in=<list_of_str>
```

##### ارتباط با مدل کتگوری (مانند صنعتی (با گروه ربات) و ...)

* لیستی از همه کتگوری ها
```
/category/
```

* گرفتن یک کتگوری خاص
```
/category/<num:id>/
/category/?id=<num>/
```

* گرفتن یک کتگوری با عنوان خاص
```
/category/?title__exact=<str>/
/category/?title__icontains=<str>
/category/?title__in=<list_of_str>
```

این مدل با گروه رابطه دارد پس رابطه تو در تو مانند جاهای دیگر این طراحی قابل انجام است

* لیستی از کتگوری هایی که در گروه خاص هستند
```
/category/?group__id=<num:id>/
/category/?group__id__in=<list_of_integer>/
```

* لیستی از کتگوری هایی که در گروه با عنوان خاص هستند
```
/category/?group__title=<str>/
/category/?group__str__in=<list_of_str>/
/category/?group__str__icontains=<str>/
```