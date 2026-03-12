export type Repo = {
    name: string;
    stargazerCount: number;
}

export type Student = {
    username: string;
    score: number;
    stars: number;
    commits: number;
    prs: number;
    repos: number;
    followers: number;
    rank: number;
    top5repos: Repo[];
};
