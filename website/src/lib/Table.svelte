<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import { rankStudents, giveMedal } from "./rank";

    let query = $state("");

    const rankedStudents = (async ()=>await rankStudents())();
</script>

<SearchBar bind:query={query}/>

<div>
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
                    <td>{giveMedal(student.rank)}{student.rank}</td>
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
    div {
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

</style>
