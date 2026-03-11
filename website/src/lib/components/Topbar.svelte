<script lang="ts">
    const { openSideMenu } = $props();

    const fetchData = (async () => {
        const response = await fetch('data/fetchdata.json');
        const data = await response.json();
        return data;
    })()
</script>

<header>
    <button class="hamburger" aria-label="Open Side Menu" onclick={openSideMenu}>
        <img src="assets/hamburger.svg" alt="">
    </button>

    <h1>
        LEIC GitHub Leaderboards
    </h1>

    <div class="last-update-time">
        {#await fetchData}
            Updated:<br>Loading...
        {:then data}
            Updated:<br>{data.date}
        {:catch error}
            Updated:<br>Couldn't fetch last update time
        {/await}
    </div>
</header>

<style>
    header {
        background-color: var(--bg-2);
        border-bottom: 4px solid var(--bg-3);
        height: 5rem;

        color: white;

        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    }

    h1 {
        font-family: "Space Grotesk", sans-serif;
        font-weight: 500;
        font-style: normal;
        font-size: clamp(1.2rem, 4vw, 2.5rem);
        color: var(--text-1);

        flex-grow: 1;
        position: absolute;
        left: 50%;
        transform: translate(-50%, 0%);

        text-align: center;
    }

    div.last-update-time {
        font-family: "Raleway", sans-serif;
        font-weight: 600;
        font-size: clamp(0.5rem, 1vw, 1.5rem);

        text-align: center;

        padding-right: min(10px, 1%);

        min-height: 100%;
        display: flex;
        align-items: center;

        max-width: 25%;
        color: var(--text-1);
    }

    button.hamburger {
        height: 100%;
        width: 0;
        padding-left: min(25px, 5%);
        background-color: var(--bg-2);
        border: none;
        display: flex;
        align-items: center;
    }

    button.hamburger img {
        height: 35%;
    }

</style>
