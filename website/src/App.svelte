<script>
    import Topbar from "./lib/Topbar.svelte";
    import Table from "./lib/Table.svelte";
    import SideMenu from "./lib/SideMenu.svelte";

    let sideMenuOpen = $state(false);

    function toggleMenu() {
        sideMenuOpen = !sideMenuOpen;
    }

</script>
<svelte:head>

    <title>LEIC GitHub Leaderboards</title>

</svelte:head>

<Topbar openSideMenu={toggleMenu}/>

{#if sideMenuOpen}
    <SideMenu closeSideMenu={toggleMenu} />
{/if}

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
