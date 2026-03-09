<script>
    import Topbar from "./lib/Topbar.svelte";
    import Table from "./lib/Table.svelte";

</script>
<svelte:head>

    <title>LEIC GitHub Leaderboards</title>

</svelte:head>

<Topbar />

<main>
    <Table />
</main>

<style>

    :global(body) {
        background-color: var(--bg-1);
        margin: 0;
    }

    :global(.prevent-select) {
        user-select: none;
    }

    main {
        display: flex;
        flex-direction: column;
        align-items: center; 
        
        margin-top: 3rem;
        margin-bottom: 3rem;
    }

</style>
