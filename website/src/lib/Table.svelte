<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import { rankStudents, giveMedal } from "./rank";
    import type { Student } from "./rank";

    import { fade } from "svelte/transition";
    import { flip } from "svelte/animate";
    import { onMount } from "svelte";

    let query = $state("");
    let hoveredRankIndex: number | undefined = $state(undefined);

    let students = $state<Student[]>([]);

    let sortBy: keyof Student = $state("rank");
    let sortAscending: boolean = $state(true);

    let filteredStudents = $derived(
        students.filter(student => student.username.toLowerCase().includes(query.toLowerCase()))
        .sort((a:Student, b:Student)=>{
            const valA = a[sortBy];
            const valB = b[sortBy];

            if (typeof valA === 'string' && typeof valB === 'string') {
                const strA = valA as string;
                const strB = valB as string;
                return sortAscending 
                    ? strA.localeCompare(strB) 
                    : strB.localeCompare(strA);
            }

            return sortAscending 
                ? (valA as number) - (valB as number) 
                : (valB as number) - (valA as number);
        })
    );

    onMount(async () => {
        students = await rankStudents();
    });
    
    function changeSort(newSortBy: keyof Student) {
        if (sortBy === newSortBy) {
            sortAscending = !sortAscending;
        }
        else {
            const naturallyAscending = ["rank", "username"];
            sortAscending = naturallyAscending.includes(newSortBy);
            sortBy = newSortBy;
        }
    }

    let selectedAnyHeader: boolean = $state(false);

    function getSortArrow(): string {
        if (!selectedAnyHeader) {return ""};
        return (sortAscending ? "⬆" : "⬇");
    }
    

</script>

<SearchBar bind:query={query}/>

<div class="table">
<table>
    <thead>
        <tr>
            <th style="width: 10%;" onclick={()=>{changeSort("rank");selectedAnyHeader=true}}>
                Rank {sortBy==="rank" ? (getSortArrow()) : ""}
            </th>
            <th style="width: 30%;" onclick={()=>{{changeSort("username");selectedAnyHeader=true}}}>
                GitHub {sortBy==="username" ? (getSortArrow()) : ""}
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("stars");selectedAnyHeader=true}}>
                Stars {sortBy==="stars" ? (getSortArrow()) : ""}
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("prs");selectedAnyHeader=true}}>
                PRs {sortBy==="prs" ? (getSortArrow()) : ""}
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("commits");selectedAnyHeader=true}}>
                Commits {sortBy==="commits" ? (getSortArrow()) : ""}
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("followers");selectedAnyHeader=true}}>
                Followers {sortBy==="followers" ? (getSortArrow()) : ""}
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("repos");selectedAnyHeader=true}}>
                Repos {sortBy==="repos" ? (getSortArrow()) : ""}
            </th>
        </tr>
    </thead>

    <tbody>
        {#if students.length === 0}
            <tr>
                <td colspan=7>Loading...</td>
            </tr>
        {:else} 
            
            {#each filteredStudents as student, i (student.username)}
                <tr>
                    <td onmouseenter={() => hoveredRankIndex = i} onmouseleave={() => hoveredRankIndex = undefined}>
                        {giveMedal(student.rank)}{student.rank}
                        {#if hoveredRankIndex === i}
                            <div class="score-viewer" transition:fade={{duration:200}}>{student.score.toFixed(1)}</div>
                        {/if}
                    </td>
                    <td onclick={()=>window.open(`https://github.com/${student.username}`)}>
                        {student.username}
                    </td>
                    <td>{student.stars}</td>
                    <td>{student.prs}</td>
                    <td>{student.commits}</td>
                    <td>{student.followers}</td>
                    <td>{student.repos}</td>
                </tr>
            {/each}

            <tr class="padding-row">
                <td colspan=7></td>
            </tr>

        {/if}
    </tbody>
</table>
</div>

<style>
    div.table {
        margin-top: 2rem;
        height: 65vh;
        overflow-y: scroll;
        overflow-x: auto;
        border-radius: 20px;
        max-width: 95vw;
        background-color: var(--table-row-1);
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

        user-select: none;

        transition: color 0.2 ease-in-out;
    }

    th:hover {
        color: var(--accent-1);
    }

    td {
        text-align: center;

        color: var(--text-1);

        font-family: "Inter", sans-serif;
        font-weight: 400;

        padding: 8px 0 8px 0;

        font-size: 1rem;

        position: relative;
        
        transition: color 0.2s ease-in-out;

        user-select: none;
    }

    td:hover {
        color: var(--accent-1);
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
