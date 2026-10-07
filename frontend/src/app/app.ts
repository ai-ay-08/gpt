import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  article: string = '';
  summary: string = 'Your summary will appear here.';

  summarizeArticle() {
    console.log(this.article);

    this.summary = "what the fuck is " + this.article;
  }
}