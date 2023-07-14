<script>
    import Nested from "./Nested.svelte";

    let src = "/image.gif";
    let name = "bob";

    let raw = `hello <strong>world</strong>`;

    import PackageInfo from "./PackageInfo.svelte";

    const pkg = {
        name: "svelte",
        version: 3,
        speed: "blazing",
        website: "https://svelte.dev",
    };
</script>

<img src={src} alt="{name} is dancing." />
<img {src} alt="{name} is dancing." />

<!-- regular javascript can be used in {} -->
<p>This is {name.toUpperCase()} paragraph.</p>

<!-- imported component will not be impacted by local style -->
<Nested answer={42} />
<!-- {...pkg} is like {src} for object instead of enumerate one by one -->
<PackageInfo {...pkg} />
<PackageInfo name={pkg.name} />

<!-- to return unescaped HTML -->
<p>{@html raw}</p>

<style>
    /* scoped to this component */
    p {
        color: purple;
        font-family: "Comic Sans MS", cursive;
        font-size: 2em;
    }
</style>
