<script>
    // must be called when the component is first instantiated
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    function sayHello() {
        dispatch("custommsg", {
            text: "hello bob",
        });
    }
</script>

<button on:click={sayHello}> Click to say hello </button>
