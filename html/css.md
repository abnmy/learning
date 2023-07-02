# CSS

CSS, Cascading Style Sheet

**note :** browsers have a default stylesheet > [reset](https://en.wikipedia.org/wiki/Reset_style_sheet) ?

## Anatomy

```css
/* example.css */

selector {
    property: value;
}

p {
    color: red;
}

#id {}

.class {}

input[type=submit] {}. /* attribute selector */
```

```html
<html>
    <head>
        <link type="text/css" rel="stylesheet" href="example.css">
        <style>
            p {
                color: yellow;
            }
        </style>
    </head>

    <body>
        <p style="color:blue;">Hello World</p>
    </body>
</html>
```

## Rule

Typically, the order dose not matter in CSS. If an attribute is defined several times, the last definition is the one applied.

From generic to specific. First, declare the broadest rules with type selectors, and then, get more specific with class selectors.

## Box Model

1. content area
2. padding surround content
3. border surround padding
4. margin surround border

Each side can be defined individually.

```css
h2 {
    padding: 6px 3px 0 0;  /* top right bottom left */
}
```

## Centering

An entire block-level tag (div) with a fixed-width, set margin left and right to `auto`.

Inside block-level tag, set text-align to `center`.

Image can be display as `block` and centered with `margin: auto` technique.

## Background

```css
body {
    background: #5f5f5f url(images/bg.png) top left repeat;
}
```

## Fonts

```css
p {
    font-family: Helvetica, Arial, sans-serif;
    line-height: 20px;
}
```