<script>
    async function getRandomNumber() {
        const res = await fetch(`https://svelte.dev/tutorial/random-number`);
        const text = await res.text();

        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    // init
    let promise = getRandomNumber();

    // update
    function handleClick() {
        promise = getRandomNumber();
    }
</script>

<button on:click={handleClick}> generate random number </button>

{#await promise}
    <p>wait...</p>
{:then number}
    <p>{number}</p>
{:catch error}
    <p>{error.message}</p>
{/await}

<!-- can be simplified -->
{#await promise then number}
    <p>{number}</p>
{/await}
