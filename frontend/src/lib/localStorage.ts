
export namespace LocalStorage {
    export namespace CurrentUserId {
        export function get() {
            return localStorage.getItem('mixMasterCurrentUserId');
        }

        export function set(id: string) {
            localStorage.setItem('mixMasterCurrentUserId', id);
        }

        export function remove() {
            localStorage.removeItem('mixMasterCurrentUserId');
        }
    }

    export namespace CurrentProjectId {
        export function get() {
            return localStorage.getItem('mixMasterCurrentProjectId');
        }

        export function set(id: string) {
            localStorage.setItem('mixMasterCurrentProjectId', id);
        }

        export function remove() {
            localStorage.removeItem('mixMasterCurrentProjectId');
        }
    }


    export namespace CurrentMixId {
        export function get() {
            return localStorage.getItem('mixMasterCurrentMixId');
        }

        export function set(id: string) {
            localStorage.setItem('mixMasterCurrentMixId', id);
        }

        export function remove() {
            localStorage.removeItem('mixMasterCurrentMixId');
        }
    }
}