import matplotlib.pyplot as plt
import pandas as pd


class SteamStats:

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(self.filepath)
        self.counts = self._get_counts()

    def _get_counts(self): 
        
        countries = self.df["country"].dropna()
        return countries.value_counts()

    def plot(
        self,
        top_n = 10,  
        scale = 1000, 
        legend_label = "В тысячах",
        save_path = None,
        figsize = (10, 6)
    ):
        data = self.counts.head(top_n) if top_n else self.counts

        labels = list(data.index)
        values = [v / scale for v in data.values]

        if top_n is None and len(labels) > 20:
            figsize = (max(14, len(labels) * 0.6), 7)

        _, ax = plt.subplots(figsize=figsize)
        bars = ax.bar(labels, values, color="#4472C4", width=0.5)
        
        ax.set_title("Количество игроков Steam", fontsize=15, pad=15)
        
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
            
        ax.yaxis.grid(True, linestyle="-", alpha=0.5)
        ax.set_axisbelow(True)
        ax.set_xlabel("Страна", fontsize=12, labelpad=10)
        ax.set_ylabel("Количество игроков", fontsize=12, labelpad=10)
        
        rotation = 90 if len(labels) > 15 else 45
        ax.tick_params(axis="x", rotation=rotation, labelsize=10, length=0)
        ax.tick_params(axis="y", labelsize=11, length=0)
        
        for tick in ax.get_xticklabels():
            tick.set_horizontalalignment("right")

        # Легенда
        ax.legend(
            [bars[0]],
            [legend_label],
            loc="lower center",
            bbox_to_anchor=(0.5, -0.25),
            frameon=False,
            fontsize=11
        )
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
            print(f"График сохранён: {save_path}")
            
        plt.show()