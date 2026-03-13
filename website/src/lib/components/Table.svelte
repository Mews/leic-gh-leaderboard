<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import Tooltip from "./Tooltip.svelte";
    import { rankStudents, giveMedal } from "../scripts/rank";
    import type { Student } from "../scripts/types";
    import { tooltip_state } from "../scripts/tooltip_state.svelte";

    import { fade } from "svelte/transition";
    import { flip } from "svelte/animate";
    import { onMount } from "svelte";

    let query = $state("");

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

    function getSortArrow() {
        return (sortAscending ? 
            "assets/up-arrow.svg" : 
            "assets/down-arrow.svg"
        );
    }
    

</script>

<SearchBar bind:query={query}/>

<div class="table minimal-scrollbar">
<table>
    <thead>
        <tr>
            <th style="width: 8.5%;" onclick={()=>{changeSort("rank");selectedAnyHeader=true}}>
                <div class="header-text">
                    Rank
                    {#if sortBy === "rank" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
            </th>
            <th style="width: 30%;" onclick={()=>{{changeSort("username");selectedAnyHeader=true}}}>
                <div class="header-text">
                    GitHub
                    {#if sortBy === "username" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("stars");selectedAnyHeader=true}}>
                <div class="header-text">
                    Stars
                    {#if sortBy === "stars" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("prs");selectedAnyHeader=true}}>
                <div class="header-text"> 
                    PRs
                    {#if sortBy === "prs" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("commits");selectedAnyHeader=true}}>
                <div class="header-text">
                    Commits
                    {#if sortBy === "commits" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
            </th>
            <th style="width: 13.5%;" onclick={()=>{changeSort("followers");selectedAnyHeader=true}}>
                <div class="header-text">
                    Followers
                    {#if sortBy === "followers" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
            </th>
            <th style="width: 12%;" onclick={()=>{changeSort("repos");selectedAnyHeader=true}}>
                <div class="header-text">
                    Repos
                    {#if sortBy === "repos" && selectedAnyHeader}
                        <span class="header-sort-indicator" style="mask: url('{getSortArrow()}'); mask-size: contain;">
                        </span>
                    {/if}
                </div>
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
                    <td 
                        onmousemove={(e) => {
                            tooltip_state.x = e.pageX + 15;
                            tooltip_state.y = e.pageY - 10;
                            tooltip_state.html = student.score.toFixed(1);
                            tooltip_state.show = true;
                        }}
                        onmouseleave={()=>tooltip_state.show=false}
                        >
                        {giveMedal(student.rank)+student.rank}
                    </td>
                    <td onclick={()=>window.open(`https://github.com/${student.username}`)}
                        onmousemove={(e) => {
                            tooltip_state.x = e.pageX + 15;
                            tooltip_state.y = e.pageY - 10;
                            tooltip_state.html = 
                            `Click to open ${student.username}'${student.username.endsWith("s") ? "" : "s"} profile`;
                            tooltip_state.show = true;
                        }}
                        onmouseleave={()=>tooltip_state.show=false}>
                        {student.username}
                    </td>
                    <td
                        onmousemove={(e) => {
                            tooltip_state.x = e.pageX + 15;
                            tooltip_state.y = e.pageY - 10;
                            tooltip_state.html = `<strong>${student.username}'s top 5 repos</strong><br>` +
                            student.top5repos.map(repo=>`⭐${repo.stargazerCount} - ${repo.name}`).join("<br>");
                            tooltip_state.show = true;
                        }}
                        onmouseleave={()=>tooltip_state.show=false}
                        onclick={()=>window.open(`https://github.com/${student.username}?tab=repositories&sort=stargazers`)}>
                        {student.stars}
                    </td>
                    <td>{student.prs}</td>
                    <td>{student.commits}</td>
                    <td>{student.followers}</td>
                    <td
                        onmousemove={(e) => {
                            tooltip_state.x = e.pageX + 15;
                            tooltip_state.y = e.pageY - 10;
                            tooltip_state.html = `<strong>${student.username}'s top 5 repos</strong><br>` +
                            student.top5repos.map(repo=>`⭐${repo.stargazerCount} - ${repo.name}`).join("<br>");
                            tooltip_state.show = true;
                        }}
                        onmouseleave={()=>tooltip_state.show=false}
                        onclick={()=>window.open(`https://github.com/${student.username}?tab=repositories&sort=stargazers`)}>
                        {student.repos}
                    </td>
                </tr>
            {/each}

            <tr class="padding-row">
                <td colspan=7 class="padding-row">
                    {#if filteredStudents.length === 0}
                        No students found!
                    {/if}
                </td>
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

        scrollbar-color: var(--scrollbar-thumb) var(--scrollbar-track);
        box-shadow: 0px 0px 50px var(--accent-2);
    }

    table {
        table-layout: fixed;
        border-collapse: collapse;

        width: min(95vw, 60rem);

        min-width: 950px;

        height: 100%;
    }

    th {
        background-color: var(--table-header);

        color: var(--text-header);

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

    div.header-text {
        position: relative;
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
    }

    th:hover {
        color: var(--text-hover);
    }

    span.header-sort-indicator {
        position: absolute;

        right: -24px;
        bottom: -0px;

        height: 22px;
        width: 22px;

        background-color: currentColor;
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

    td:hover:not(.padding-row) {
        color: var(--text-hover);
        transform: scale(1.1);
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
