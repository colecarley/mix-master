import { goto } from "$app/navigation";
import { post } from "./helpers";
import { LocalStorage } from "./localStorage";


class Session {
    async login(username: string, password: string) {
        const response = await post("/login/", {
            username,
            password,
        });

        if (response.ok) {
            const { id } = await response.json();

            LocalStorage.CurrentUserId.set(id);
            goto("/projects");
        } else {
            console.error("error");
        }
    }

    logout() {
        LocalStorage.CurrentUserId.remove();
        LocalStorage.CurrentProjectId.remove();
        LocalStorage.CurrentMixId.remove();

        goto("/");
    }
};

const SessionInstance = new Session();
Object.freeze(SessionInstance);
export default SessionInstance;