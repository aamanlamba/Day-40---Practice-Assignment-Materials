import { Component, Input } from '@angular/core';
@Component({selector:'legacy-widget', standalone:true, template:`<div [innerHTML]="html"></div>`})
export class LegacyWidgetComponent { @Input() html=''; }
