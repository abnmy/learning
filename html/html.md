# HTML

ARIA, Accessible Rich Internet Applications

HTML, HyperText Markup Language, add informations/instructions to render a document (text, images, etc.) in web browser.

HTTP, HyperText Transport Protocol, is the method to exchange HTML documents.

URI, Universal Resource Identifier,

URL, Universal Resource Locator,

## Element

An element is a component of a webpage. The content is surrounded by tags. Tags could have one or several attributes.

```html
<div attribute="xyz" >  <!-- opening tag -->
    content
</div> <!-- closing tag -->

<img src="picture.jpg" size="150px" /> <!-- auto closing tag -->

<br />
```

https://en.wikipedia.org/wiki/HTML_element

## Quick Templates

```html
<!DOCTYPE HTML>
<html>
    <head> <!-- metadata adds context does not impact render -->
        <title>Page Title</title>
    </head>

    <body>
        <p>Hello World!</p>
    </body>
</html>
```

```html
<!DOCTYPE HTML> <!-- HTML 5 version -->
<html> <!-- root element -->
    <head>
        <title>Page Title</title>
        <meta name="description" content="demo">
        <script>
        <style>
        <link rel="stylesheet">
        <base>
    </head>

    <body>
        <p>Hello World!</p>
    </body>
</html>
```

## Ressources and Tools

https://validator.w3.org/#validate_by_input

https://developer.mozilla.org/

https://caniuse.com/

## Block VS Inline

Block elements (e.g. div, h1, p, ul) may contain block or inline elements. The content of block-level tags take up the entire width of the container.

Inline elements (e.g. span, a, img, input) may contain inline elements.

`display` attribute allow to change element type 

## Whitespaces

```
&nbsp; 
<br />
```

## Anchor
```html
<a href="#brownies"></a>
<div id="brownies"></div>
```

## Image

```html
<img
    src="xyz.png"
    alt="image description for, at least, screen readers"
    srcset=""
    sizes="(max-width: 500px) 15vw, 25vw"
/>

<picture>
    <source srcset="photo.avif" type="image/avif" />
    <source srcset="photo.webp" type="image/webp" />
    <img src="photo.jpg" alt="photo" />
</picture>
```

## Table

```html
<table>
    <caption></caption>
    <thead>
        <tr>
            <th rowspan="2"></th>
            <th></th>
            <!-- <th></th> -->
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tfoot>
</table>

```

## Forms

```html
<form>
    <label for="user-name">Name</label>
    <input type="text" id="user-name" />
    <textarea></textarea> <!-- no type! -->
    <input type="submit" value="Click" />
</form>
```

## Accessibility

https://www.w3.org/TR/html-aria/