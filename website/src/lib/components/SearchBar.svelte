<script lang="ts">
    export let query = "";
</script>

<input bind:value={query} placeholder="Search for someone..."/>

<style>
    input {
        background-color: var(--bg-1);
        border: none;
        border-bottom: 4px solid var(--accent-1);

        color: var(--text-1);

        outline: none;

        width: 50vw;

        font-family: "Raleway", sans-serif;
        font-weight: 500;

        transition: 
            width 0.3s ease-in-out,
            border-bottom 0.3s ease-in-out,
            padding-left 0.3s ease-in-out,
            transform 0.3s ease-in-out;
    }

    input:focus {
        width: 53vw;
        border-bottom: 4px solid var(--accent-2);
        padding-left: 1rem;
        transform: translateY(-2px) scale(1.05);
    }



    ::placeholder {
        color: var(--text-1);
        opacity: 1;
    }

    ::-ms-input-placeholder {
        color: var(--text-1);
    }

</style>
