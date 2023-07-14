<script>
    let count = 0;
    $: doubled = count * 2; // reactive declarations
    function increment() {
        count += 1;
    }

    // reactive declarations can be used for statement
    $: console.log(`the count is ${count}`); // ${count} is string interpolation
    $: {
    }
    $: if (true) {
    }
    // Svelte's reactivity is triggered by **assignments**,
    // array methods like push and splice won't cause updates
    let numbers = [1, 2, 3, 4];

    function addNumber() {
        // numbers.push(numbers.length + 1);
        // numbers = numbers;
        numbers = [...numbers, numbers.length + 1];
    }
    $: sum = numbers.reduce((t, n) => t + n, 0);
</script>

<!-- event handler with `on:` directives -->
<!-- the DOM is updated when the component's state changes -->
<button on:click={increment}>
    Clicked {count}
    {count === 1 ? "time" : "times"}
</button>
<p>{count} doubled is {count * 2}</p>
<!-- better if used multiple times -->
<p>{count} doubled is {doubled}</p>

<p>{numbers.join(" + ")} = {sum}</p>

<button on:click={addNumber}> Add a number </button>
