<script lang="ts">
    import Topbar from "./lib/components/Topbar.svelte";
    import Table from "./lib/components/Table.svelte";
    import SideMenu from "./lib/components/SideMenu.svelte";
    import Modal from "./lib/components/Modal.svelte";

    import { marked } from "marked";

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

    const openingModalMarkdown = `
# Hey there!

This is a website where LEIC students are ranked based on their GitHub stats.

If you see your username in the leaderboard and you don't want to, or if you want to be in the leaderboard but aren't yet,
feel free to reach out to me!

You can find my contact information in the side menu.

**And remember, this is all for fun :)**<br>Have fun climbing the leaderboard!
`;

    setTimeout(async () => {
        const html = await marked.parse(openingModalMarkdown);
        showModal(html);
    }, 1);

    let lightModeEnabled = $state(localStorage.getItem("theme") === "light");

    $effect(() => {
        const mode = lightModeEnabled ? "light" : "dark";
        localStorage.setItem("theme", mode);
        
        if (lightModeEnabled) {
            document.documentElement.classList.add("light-mode");
        } else {
            document.documentElement.classList.remove("light-mode");
        }
    });

</script>
<svelte:head>

    <title>LEIC GitHub Leaderboards</title>

</svelte:head>

<Topbar openSideMenu={toggleMenu}/>

{#if sideMenuOpen}
    <SideMenu closeSideMenu={toggleMenu} {showModal} bind:lightModeEnabled={lightModeEnabled}/>
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
