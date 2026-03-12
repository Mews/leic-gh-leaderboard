<script lang="ts">
    import { tooltip_state } from "../scripts/tooltip_state.svelte";
    import { fade } from "svelte/transition";
</script>

{#if tooltip_state.show}
    <div class="tooltip" style="top: {tooltip_state.y}px; left: {tooltip_state.x}px;"
        transition:fade={{duration:200}}>
        {@html tooltip_state.html}
    </div>
{/if}

<style>
    div.tooltip {
        position: absolute;

        background-color: var(--bg-1);
        color: var(--text-1);
        padding: 8px 12px;
        border-radius: 6px;
        border: 1px solid var(--accent-1);
        font-size: 0.85rem;

        font-family: "Inter", sans-serif;
        font-weight: 400;
        pointer-events: none;
    }
</style>
