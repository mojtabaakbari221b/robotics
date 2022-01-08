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

##### ارتباط با مدل ارگان (شامل رباتها و ماشین ابزار کنترل عددی)

* لیستی از همه ارگان ها
```
/organ/
```

* گرفتن یک ارگان خاص
```
/organ/<num:id>/
/organ/?id=<num>/
```

* گرفتن یک ارگان با کتگوری خاص
```
/organ/?category__id=<int>/
/organ/?category__id__in=<list_of_integer>
```

##### ارتباط با مدل درباره، تماس با ما و استاندارهای ارگان

* گرفتن یک درباره با ما
```
/info/?organ__id=<int:id>
```

* گرفتن یک تماس با ما
```
/contact/?organ__id=<int:id>
```

* گرفتن یک استاندارها
```
/standard/?organ__id=<int:id>
```

#### ارتباط با مدل محصولات

* لیستی از همه محصولات
```
/product/
```

* محصول خاص
```
/product/<num:id>/
/product/?id=<num>/
```

#### ارتباط با مدل اخبار

* لیستی از همه اخبار
```
/news/
```

* خبر خاص
```
/news/<num:id>/
/news/?id=<num>/
```

#### ارتباط با مدل نیازمندیها

* لیستی از همه نیازمندیها
```
/requirements/
```

* نیازمندی خاص
```
/requirements/<num:id>/
/requirements/?id=<num>/
```

#### ارتباط با مدل حامیان سایت

* لیستی از همه حامیان سایت
```
/site_supporter/
```

* حامی سایت خاص
```
/site_supporter/<num:id>/
/site_supporter/?id=<num>/
```

#### با مدل صفحات

* لیستی از همه صفحات
```
/site_supporter/
```

* صفحه خاص
```
/page/<num:id>/
/page/?id=<num>/
```