<script>
    // !not classic export usage!
    // exposed properties (props)
    export let answer = "default value is facultative";

    // !not recommended!
    // $$props allow to access all the props passed into a component
    // ...even those that have not been declared
    $$props;
</script>

<p>The answer is {answer}</p>
