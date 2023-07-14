<script>
    import Inner from "./EventComponent.svelte";
    let m = { x: 0, y: 0 };

    function handleMousemove(event) {
        m.x = event.clientX;
        m.y = event.clientY;
    }
    function handleClick() {
        alert("clicked");
    }
    function handleMessage(event) {
        alert(event.detail.text);
    }
</script>

<!-- event handler with `on:` directives -->
<div on:mousemove={handleMousemove}>
    The mouse position is {m.x} x {m.y}
</div>

<!-- inline -->
<!-- there is no perfomance issue thanks to svelte compiler -->
<div on:mousemove={(e) => (m = { x: e.clientX, y: e.clientY })}>
    The mouse position is {m.x} x {m.y}
</div>

<!--
The full list of modifiers:

preventDefault — calls event.preventDefault() before running the handler. Useful for client-side form handling, for example.
stopPropagation — calls event.stopPropagation(), preventing the event reaching the next element
passive — improves scrolling performance on touch/wheel events (Svelte will add it automatically where it's safe to do so)
nonpassive — explicitly set passive: false
capture — fires the handler during the capture phase instead of the bubbling phase (MDN docs)
once — remove the handler after the first time it runs
self — only trigger handler if event.target is the element itself
trusted — only trigger handler if event.isTrusted is true. I.e. if the event is triggered by a user action.
 -->
<!-- You can chain modifiers -->
<button on:click|once|capture={handleClick}> Click me </button>

<!-- dispatch event -->
<Inner on:custommsg={handleMessage} />

<!-- event forwarding -->
<!-- on:custommsg is a shorcut fo nested components -->
<!-- w/o values means forward all `custommsg` events -->
<Inner on:custommsg />

<!-- DOM event forwarding -->
<!-- <button on:click>Click me</button> -->
<CustomButton on:click={handleClick} />

<style>
    div {
        width: 100%;
        height: 100%;
    }
</style>
