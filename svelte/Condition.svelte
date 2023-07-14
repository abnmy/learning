<script>
    let x = 42;
    let user = { loggedIn: false };

    function toggle() {
        user.loggedIn = !user.loggedIn;
    }
</script>

{#if user.loggedIn}
    <button on:click={toggle}> Log out </button>
{/if}
{#if !user.loggedIn}
    <button on:click={toggle}> Log in </button>
{/if}

<!-- :else (:) indicates a block continuation tag  -->
{#if user.loggedIn}
    <button on:click={toggle}> Log out </button>
{:else}
    <button on:click={toggle}> Log in </button>
{/if}

<!-- else if -->
{#if x > 10}
    <p />
{:else if x > 5}
    <p />
{:else}
    <p />
{/if}
