<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import { rankStudents, giveMedal } from "./rank";

    import { fade } from "svelte/transition";

    let query = $state("");
    let hoveredRankIndex: number | undefined = $state(undefined);

    const rankedStudents = (async ()=>await rankStudents())();
</script>

<SearchBar bind:query={query}/>

<div class="table">
<table>
    <thead>
        <tr>
            <th style="width: 10%;">Rank</th>
            <th style="width: 30%;">GitHub</th>
            <th style="width: 12%;">Stars</th>
            <th style="width: 12%;">PRs</th>
            <th style="width: 12%;">Commits</th>
            <th style="width: 12%;">Followers</th>
            <th style="width: 12%;">Repos</th>
        </tr>
    </thead>

    <tbody>
        {#await rankedStudents}
            <tr>
                <td colspan=7>Loading...</td>
            </tr>
        {:then students} 
            
            {#each students as student, i}
                {#if student.username.toLowerCase().includes(query.toLowerCase())}
                <tr>
                    <td onmouseenter={() => hoveredRankIndex = i} onmouseleave={() => hoveredRankIndex = undefined}>
                        {giveMedal(student.rank)}{student.rank}
                        {#if hoveredRankIndex === i}
                            <div class="score-viewer" transition:fade={{duration:200}}>{student.score.toFixed(1)}</div>
                        {/if}
                    </td>
                    <td>{student.username}</td>
                    <td>{student.stars}</td>
                    <td>{student.prs}</td>
                    <td>{student.commits}</td>
                    <td>{student.followers}</td>
                    <td>{student.repos}</td>
                </tr>
                {/if}
            {/each}

            <tr class="padding-row">
                <td colspan=7></td>
            </tr>

        {/await}
    </tbody>
</table>
</div>

<style>
    div.table {
        margin-top: 2rem;
        height: 65vh;
        overflow: auto;
        border-radius: 20px;
        max-width: 95vw;
    }

    table {
        table-layout: fixed;
        border-collapse: collapse;

        width: min(95vw, 60rem);

        min-width: 750px;

        height: 100%;
    }

    th {
        background-color: var(--table-header);

        color: var(--text-2);

        font-family: "Raleway", sans-serif;
        font-weight: 600;
        font-size: 1.1rem;

        position: sticky;
        top: 0;
        z-index: 10;

        padding: 10px 0 10px 0;
    }

    td {
        text-align: center;

        color: var(--text-1);

        font-family: "Inter", sans-serif;
        font-weight: 400;

        padding: 8px 0 8px 0;

        font-size: 1rem;

        position: relative;
    }

    tr:nth-child(odd) {
        background-color: var(--table-row-1);
    }

    tr:nth-child(even) {
        background-color: var(--table-row-2);
    }

    tr.padding-row {
        height: 100%;
    }

    div.score-viewer {
        position: absolute;
        top: 50%; 
        left: 50%;
        transform: translate(25px, -50%);
    
        background-color: var(--bg-1);
        color: var(--text-1);
        padding: 8px 12px;
        border-radius: 6px;
        border: 1px solid var(--accent-1);
        font-size: 0.85rem;

        z-index: 100;

        font-family: "Inter", sans-serif;
        font-weight: 400;
    }

</style>
