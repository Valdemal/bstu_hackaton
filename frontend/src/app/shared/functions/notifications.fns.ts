export function notify(message: string, duration: number = 3400){
    alert(message);
    //Переработать, реализовать блок уведомления в нижней части экрана
    setTimeout(() => hide(), duration);
}

export function hide(){
    //...
}