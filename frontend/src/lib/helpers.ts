import { LOCAL_HOST } from "./settings"

export function post(url: string, data: Record<string, any>) {
    return fetch(`${LOCAL_HOST}${url}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
}

export function get(url: string) {
    return fetch(`${LOCAL_HOST}${url}`);

}

export function formatDate(date: string) {
    return new Date(date).toLocaleDateString('en-US');
}


