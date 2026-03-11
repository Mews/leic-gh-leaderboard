<script>
    import { fly, fade } from "svelte/transition";

    let { body, hideModal } = $props();

</script>

<button class="backdrop" transition:fade={{duration:200}} onclick={hideModal} aria-label="Close Modal"></button>

<div id="modal-outer" transition:fly={{duration:750, y:-700}}>
    <div id="modal" class="minimal-scrollbar">
        {@html body}
    </div>
</div>


<style>
    .backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(2px);
        z-index: 499;
    }

    div#modal-outer {
        overflow-y: hidden; 
        border-radius: 25px; 
        height: 60vh; 
        width: 50vw;

        position: absolute;
        left: 0;
        right: 0;
        margin-inline: auto;
        top: 15%;

        z-index: 500;

        box-shadow: 0px 0px 10px var(--accent-1);

        padding: 2rem;

        background-color: var(--bg-1);
    }

    div#modal {

        color: var(--text-1);
        
        overflow-y: auto;

        height: 100%;

        font-family: "Raleway", sans-serif;

        padding-right: 1rem;
    }

    /* Styles for markdown */
    div#modal :global(h1) {
        margin: 0;
        color: var(--text-2);
    }

    div#modal :global(h2) {
        font-size: 1.3rem;
        font-weight: 600;
    }

    div#modal :global(p) {
        padding-left: 1rem;
    }

    div#modal :global(a) {
        color: var(--accent-1);
    }

</style>
