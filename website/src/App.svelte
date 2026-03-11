<script lang="ts">
    import Topbar from "./lib/Topbar.svelte";
    import Table from "./lib/Table.svelte";
    import SideMenu from "./lib/SideMenu.svelte";
    import Modal from "./lib/Modal.svelte";

    let sideMenuOpen = $state(false);

    function toggleMenu() {
        sideMenuOpen = !sideMenuOpen;
    }


    let modalVisible = $state(false);
    let modalBody = $state("");

    function showModal(newModalBody: string) {
        modalBody = newModalBody;
        modalVisible = true;
    }

    function hideModal() {
        modalVisible = false;
    }

</script>
<svelte:head>

    <title>LEIC GitHub Leaderboards</title>

</svelte:head>

<Topbar openSideMenu={toggleMenu}/>

{#if sideMenuOpen}
    <SideMenu closeSideMenu={toggleMenu} {showModal}/>
{/if}

<main>
    <Table />
</main>
    

{#if modalVisible}
    <Modal body={modalBody} {hideModal}/>
{/if}


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

    :global(.hide-scrollbar) {
        scrollbar-width: none;
        -ms-overflow-style: none;
        
        &::-webkit-scrollbar {
            display: none;
        }
    }

    :global(.minimal-scrollbar) {
        scrollbar-color: var(--accent-1) transparent;
        scrollbar-width: thin;

        &::-webkit-scrollbar {
            width: 8px; 
        }

        &::-webkit-scrollbar-thumb {
            background-color: var(--accent-1);
            border-radius: 10px;

            border-right: 5px solid transparent;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;

            background-clip: padding-box; 
        }

        &::-webkit-scrollbar-track {
            background: transparent;
        }
    }

</style>
