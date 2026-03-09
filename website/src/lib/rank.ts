export type Student = {
    username: string;
    score: number;
    stars: number;
    commits: number;
    prs: number;
    repos: number;
    followers: number;
    rank: number;
};

export async function rankStudents() {
    const response = await fetch('data/userdata.json');
    const students = await response.json();

    students.forEach(
        (student: Student) => {
            student.score = (student.stars * 50) + 
                            (student.commits * 1) +
                            (student.prs * 3.5) + 
                            (student.repos * 1) + 
                            (student.followers * 1);
        }
    );

    students.sort((a: Student, b: Student) => {
    return  (b.score - a.score)         ||
            (b.stars - a.stars)         ||
            (b.prs - a.prs)             ||
            (b.commits - a.commits)     ||
            (b.followers - a.followers) ||
            (b.repos - a.repos)         ||
            a.username.localeCompare(b.username);
    });

    students.forEach(
        (student: Student, i:number) => {
            student.rank = i+1;
        }
    )
    
    return students;
}

export function giveMedal(rank: number) {
    switch (rank) {
        case 1:
            return '🥇';
        case 2:
            return '🥈';
        case 3:
            return '🥉';
        default:
            return '';
    }
}
