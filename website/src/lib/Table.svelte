<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    let query = $state("");

    const userData = (async () => {
        const response = await fetch('userdata.json');
        const data = await response.json();
        return data;
    })()
</script>

<SearchBar bind:query={query}/>

<div>
<table>
    <thead>
        <tr>
            <th style="width: 10%;">#</th>
            <th style="width: 30%;">GitHub</th>
            <th style="width: 12%;">Stars</th>
            <th style="width: 12%;">Commits</th>
            <th style="width: 12%;">Followers</th>
            <th style="width: 12%;">Repos</th>
            <th style="width: 12%;">PRs</th>
        </tr>
    </thead>

    <tbody>
        {#await userData}
            <tr>
                <td colspan=7>Loading...</td>
            </tr>
        {:then users} 
            
            {#each users as user, i}
                {#if user.username.toLowerCase().includes(query.toLowerCase())}
                <tr>
                    <td>{i+1}</td>
                    <td>{user.username}</td>
                    <td>{user.stars}</td>
                    <td>{user.commits_year}</td>
                    <td>{user.followers}</td>
                    <td>{user.repos}</td>
                    <td>{user.prs}</td>
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

        min-width: 600px;

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
