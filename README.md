# Today

Create a 'dynamic' snippet that prints today's date on your document.

You can configure the format creating a file called Today.sublime-settings on your
User folder with this content:

```json
{
  "date_format":"%d/%m/%Y",
  "time_format":"%d/%m/%Y %H:%M"
}
```

The format is based on strftime. You can generate it nicely using the [strfti.me] website.

[strfti.me]: http://strfti.me/