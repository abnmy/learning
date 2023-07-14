<script>
    let cats = [
        {
            id: "J---aiyznGQ",
            name: "Keyboard Cat",
        },
        {
            id: "z_AbfPXTKms",
            name: "Maru",
        },
        {
            id: "OUtn3pvWmpg",
            name: "Henri The Existential Cat",
        },
    ];
</script>

<h1>The Famous Cats of YouTube</h1>

<ul>
    {#each cats as cat}
        <li>
            <a
                target="_blank"
                href="https://www.youtube.com/watch?v={cat.id}"
                rel="noreferrer"
            >
                {cat.name}
            </a>
        </li>
    {/each}
</ul>

<ul>
    <!-- enumerate -->
    {#each cats as cat, i}
        <li>
            <a
                target="_blank"
                href="https://www.youtube.com/watch?v={cat.id}"
                rel="noreferrer"
            >
                {i + 1}: {cat.name}
            </a>
        </li>
    {/each}
</ul>

<ul>
    <!-- destructuring -->
    {#each cats as { id, name }, i}
        <li>
            <a
                target="_blank"
                href="https://www.youtube.com/watch?v={id}"
                rel="noreferrer"
            >
                {i + 1}: {name}
            </a>
        </li>
    {/each}
</ul>

<!-- keyed each blocks for dynamic list (like react) -->
{#each things as thing (thing.id)}
    <Thing name={thing.name} />
{/each}
