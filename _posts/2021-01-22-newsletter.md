---
title: "Meta: Newsletter"
layout: splash
header:
  image: /assets/images/unsplash-image-6.jpg
  caption: "Photo credit: [**New Language Studio**](https://newlanguagestudio.com)"
categories:
  - Continuity
tags:
  - Continuity
  - Drift
  - New Language Studio
#description:
#permalink:
---

It's pretty late Friday night. I've fallen into a soft deadline of the next full moon to send out my newsletter. It will include:

1. The introductory chapter to Improvised Learning
2. Book Review of Silo
3. Link to Webpage

I could say something like: `let me be clear. I am creating a kind of token to be placed on the board for a game called digital publishing. You signing up for this Newsletter gives strength to the token. I will try to play it well, and only make moves I believe in.`


The preferred way of using images is placing them in the `/assets/images/` directory and referencing them with an absolute path. Prepending the filename with `{% raw %}{{ site.url }}{{ site.baseurl }}/assets/images/{% endraw %}` will make sure your images display properly in feeds and such.

Standard image with no width modifier classes applied.

**HTML:**

```html
{% raw %}<img src="{{ site.url }}{{ site.baseurl }}/assets/images/filename.jpg" alt="">{% endraw %}
```

**or Kramdown:**

```markdown
{% raw %}![alt]({{ site.url }}{{ site.baseurl }}/assets/images/filename.jpg){% endraw %}
```

![Unsplash image 9]({{ site.url }}{{ site.baseurl }}/assets/images/unsplash-image-9.jpg)

Image that fills page content container by adding the `.full` class with:

**HTML:**

```html
{% raw %}<img src="{{ site.url }}{{ site.baseurl }}/assets/images/filename.jpg" alt="" class="full">{% endraw %}
```

**or Kramdown:**

```markdown
{% raw %}![alt]({{ site.url }}{{ site.baseurl }}/assets/images/filename.jpg)
{: .full}{% endraw %}
```

![Unsplash image 10]({{ site.url }}{{ site.baseurl }}/assets/images/unsplash-image-10.jpg)
{: .full}
